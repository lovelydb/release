#!/usr/bin/env python

import sys
import os
import os.path
import glob
import distutils.dir_util
import re
import getopt

import pdb

sys.path += [ '../pyutils' ]

import packaging
import config
import utils
import rpm_utils


def get_rpm_install(env_obj, archive=False):
	return_text = ""

	# Don't display repository information for archive pages
	if archive:
		return return_text

	# For rhel systems...
	#  If there are distro aliases, use those
	if env_obj.info.has_key('distro_aliases'):
		distro_name = env_obj.info['distro_aliases'][0]
	else:
		distro_name = env_obj.name

	# Grab OC stuff from conf file
	vars = {}
	vars['OC_DOWNLOAD_URL'] = "ftp://ftp.ximian.com/pub/redcarpet2/%s" % distro_name
	vars['OC_NOTES'] = ""
	for i in "OC_NOTES OC_DOWNLOAD_URL YUM_NOTES".split():
		if env_obj.info.has_key(i):
			vars[i] = env_obj.info[i]

	# Generate OC text
	if utils.get_dict_var('USE_OC', env_obj.info):
		return_text += """
		<p>
		This distro supports installing Mono using Novell's Red Carpet.
		If you do not already have Red Carpet, you can <a href='%s'>download</a> it.
		%s
		</p>

		<p>To use Red Carpet, execute these commands:</p>

		<xmp class='shell'>
	rug sa http://%s%s/%s
	rug sub mono-official-%s
	rug in mono-complete gtk-sharp-complete
		</xmp>

		<p>Note: some versions of Red Carpet frequently have IOError timeouts.  This is a bug in Red Carpet.  If Red Carpet for your distro frequently has this problem, please use another installation method.</p>
		""" % (vars['OC_DOWNLOAD_URL'], vars['OC_NOTES'], hostname_url, webroot_path, url_prefix, bundle_conf.info['bundle_urlname'])


	# Generate Yum Text
	if utils.get_dict_var('USE_YUM', env_obj.info):
		return_text += """
		<p>
		This distro supports installing packages via <tt>yum</tt>. Putting the
		<a href="mono.repo">mono.repo</a> file in <tt>/etc/yum.repos.d</tt> will allow you to
		install mono and related packages.
		</p>
		"""

		if utils.get_dict_var('YUM_NOTES', env_obj.info):
			return_text += """
			<p>
			%s
			</p>\n""" % vars['YUM_NOTES']

	# Generate yast text
	if utils.get_dict_var('USE_YAST', env_obj.info) or utils.get_dict_var('USE_ZMD', env_obj.info):
		return_text += """
		<p>
		This distro supports installing packages via <tt>YaST</tt>.  Add the following installation
		source to <tt>YaST</tt>:
		<ul>
		<li><tt>http://%s%s/%s/%s</tt></li>
		</ul>
		</p>
		<p>For assistance with using repositories and installing packages with YaST, visit this link: 
		<a href="http://en.opensuse.org/Add_Package_Repositories_to_YaST">[1]</a>
                </p>\n""" % (hostname_url, webroot_path, url_prefix, env_obj.name)


	# TODO: Generate zmd text
	# Hmm... zmd can use all of the above sources...
	if utils.get_dict_var('USE_ZMD', env_obj.info):
		pass

		#Only select one category, since they're all valid.
		#if OC
		#elif yum,
		#elif yast

	return return_text

def get_external_deps(env_obj, archive=False):

	if archive:	external_url_path = "../../../../external_packages"
	else:		external_url_path = "../../external_packages"

	return_text = ""

	external_rpms = glob.glob("../external_packages/%s/*.rpm" % env_obj.name)
	external_src_rpms = glob.glob("../external_packages/%s/*.src.rpm" % env_obj.name)
	
	# For the RPMS
	if external_rpms:
		return_text += "<h3>External Dependencies</h3>\n"
		return_text += "<ul>\n"
		for i in external_rpms:

			i = os.path.basename(i)

			if re.compile("\.src\.rpm").search(i):
				continue

			(NAME, DESC) = rpm_utils.rpm_query(['NAME', 'SUMMARY'], '../external_packages/%s/%s' % (env_obj.name, i) )
			return_text += "<li><a href='%s/%s/%s'>%s</a> -- %s</li>\n" % (external_url_path, env_obj.name, i, NAME, DESC)
		return_text += "</ul>\n"

	# For the source RPMS
	if external_src_rpms:
		return_text += "<p>Source RPMS: \n"
		for i in external_src_rpms:

			i = os.path.basename(i)

			NAME = rpm_utils.rpm_query('NAME', '../external_packages/%s/%s' % (env_obj.name, i) )
			return_text += "<a href='%s/%s/%s'>%s</a> \n" % (external_url_path, env_obj.name, i, NAME)

		return_text += "</p>\n"

	return return_text

# Command line options
try:
	opts, remaining_args = getopt.getopt(sys.argv[1:], "", [ "skip_zip"])
	(bundle, output_dir, webroot_path, package_src_dir, hostname_url) = remaining_args
except:
        print "Usage: ./mk-distro-index.py [--skip_zip] <bundle name> <package source dir> <output webdir> <hostname_url> <webroot_path>"
        sys.exit(1)

skip_zip = False
for option, value in opts:
        if option == "--skip_zip":
                 skip_zip = True

bundle_conf = packaging.bundle(bundle_name=bundle)
url_prefix = 'download-' + bundle_conf.info['bundle_urlname']

fd = open(os.path.join(config.release_repo_root, 'website', 'distro-index'))
template = fd.readlines()
fd.close()

version = bundle_conf.info['archive_version']
package_src_url = os.path.basename(package_src_dir)

if not package_src_url:
	print "Invalid package_src_dir, make sure it doesn't end with a slash"
	sys.exit(1)

# Go here so the rpm file globbings look right
os.chdir(package_src_dir)
distros = glob.glob(config.packaging_dir + "/conf/*-*-*")
distros.sort()
for distro_conf in distros:

	env = packaging.buildenv(os.path.basename(distro_conf))
	print "*** Generating pages for: %s" % env.name

	# Skip the distros that use zip packaging system
	if utils.get_dict_var('USE_ZIP_PKG', env.info): continue

	distro_out_dir = os.path.join(output_dir, url_prefix, env.name)
	out_file = distro_out_dir + os.sep + 'index.html'
	arc_out_file = os.path.join(output_dir, 'archive',  version, 'download', env.name, 'index.html')

	distutils.dir_util.mkpath(os.path.dirname(out_file))
	distutils.dir_util.mkpath(os.path.dirname(arc_out_file))

	out = open(out_file, 'w')
	arc_out = open(arc_out_file, 'w')

	for line in template:	
		line_segs = line.split()
		if line_segs and line_segs[0] == "#":
			ARGS = line_segs[2:]
			RPMS = []
			SPECS = []
			for package in ARGS:
				pack_obj = packaging.package(env, package, bundle_obj=bundle_conf, package_basepath=package_src_dir)

				#if pack_obj.name == "gtk-sharp": pdb.set_trace()
				if not pack_obj.valid_use_platform(env.name):
					continue

				# probably won't ever want to post zip files ... ?
				RPMS += pack_obj.get_files_relpath(ext=["rpm"], fail_on_missing=False)

				# Remove src.rpms in case we saved them (which we usually don't)
				for i in RPMS:
					if re.compile(".*\.src\.rpm").search(i):
						RPMS.remove(i)

				SPECS += pack_obj.get_files_relpath(ext="spec", fail_on_missing=False)

			if len(RPMS) == 0:
				out.write("<p>Not available for this platform</p>\n")
				arc_out.write("<p>Not available for this platform</p>\n")
				print " * Skipping " + pack_obj.name
				continue
		
			zipname = line_segs[1]
			zip_filename = distro_out_dir + os.sep + zipname + ".zip"
			if os.path.exists(zip_filename):
				os.unlink(zip_filename)

			# If there are more than one rpms to be in the zip file
			if len(RPMS) > 1 and not skip_zip:
				print "Creating zip: " + zipname
				# rpms are compressed anyways -- doing any compression is a waste of time
				os.system("zip -j -0 %s %s" % (zip_filename, " ".join(RPMS)) )
				
				out.write("<p><a href='%s.zip'><img src='/zip-icon.png' />All of these RPMs in a ZIP file</a></p>\n" % (zipname))


			out.write("<ul>\n")
			arc_out.write("<ul>\n")

			for i in RPMS:
				(NAME, DESC) = rpm_utils.rpm_query(['NAME', 'SUMMARY'], i)
				out.write("<li><a href='../../%s/%s'>%s</a> -- %s</li>\n" % (package_src_url, i, NAME, DESC) )
				arc_out.write("<li><a href='../../../../%s/%s'>%s</a> -- %s</li>\n" % (package_src_url, i, NAME, DESC) )
			
			out.write("</ul>\n")
			arc_out.write("</ul>\n")

			# Print links to spec files
			if len(SPECS) == 0:
				continue

			out.write("<p>RPM Spec files: \n")
			arc_out.write("<p>RPM Spec files: \n")
			for i in SPECS:
				NAME = os.path.basename(i)
				out.write("<a href='../../%s/%s'>%s</a> \n" % (package_src_url, i, NAME) )
				arc_out.write("<a href='../../../../%s/%s'>%s</a> \n" % (package_src_url, i, NAME) )

			out.write("</p>\n")
			arc_out.write("</p>\n")

			
		elif line_segs and line_segs[0] == "!":
			command = line_segs[1]

			# Strange... but useful way of calling a python function based on a string name
			#  always pass the buildenv object and archive bool
			out.write( eval(command)(env, archive=False) )
			arc_out.write( eval(command)(env, archive=True) )

		else:
			line = line.replace('[[arch]]', env.name)
			line = line.replace('[[version]]', version)
			line = line.replace('[[webroot_path]]', webroot_path)

			out.write(line)
			arc_out.write(line)


