var i586 = "x86 32bit (i586)";
var x86_64 = "x86 64bit (x86_64)";
var ppc = "PowerPC 32bit (ppc32)";
var ia64 = "Itanium (ia64)";
var s390 = "IBM s390 32bit";
var s390x = "IBM s390x 64bit";

suseDownloadText1 = "Your Mono packages can be found at the following URL. You can add the URL as a YaST reposit ory, or you can download the individual packages manually. <ul><li><a href='";
suseDownloadText2 = "</a></ul><br>For assistance with using repositories and installing packages with YaST, <a href='http://en.opensuse.org/Add_Package_Repositories_to_YaST'>visit opensuse.org</a>";

var data =
{
	"release" : "1.2.6",
	"platforms" : [
	{
		"name" : "VMware",
		"icon" : "vmware_icon_2.jpg",
		"dlicon" : "vmware_icon.jpg",
		"version" : [
		{
			"name" : "openSUSE 10.2",
			"arch" : [
			{
				"name" : "Mono 1.2.5.1",
				"desc" : "",
				"downloadText" : "Download the openSUSE 10.2 VMWare image which includes Mono 1.2.5.1 <ul><li><a href='http://anonsvn.mono-project.com/mono1.2.5.1_opensuse10.2_vmware_0.zip.torrent'>via Torrent</a> <li><a href='http://anonsvn.mono-project.com/mono1.2.5.1_opensuse10.2_vmware_0.zip'>via http</a> </ul><a href='http://mono-project.com/VMware_Image'>Instructions for using the VMware image</a>."
			}
			]
		}
		]
	},

	{
		"name" : "openSUSE",
		"icon" : "opensuse.jpg",
		"dlicon" : "opensuse.jpg",
		"version" : [
		{
			"name" : "openSUSE 10.1",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-i586'>http://www.go-mono.com/download-stable/suse-101-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-x86_64'>http://www.go-mono.com/download-stable/suse-101-x86_64" + suseDownloadText2
			},
			{
				"name" : ppc,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-ppc'>http://www.go-mono.com/download-stable/suse-101-ppc" + suseDownloadText2
			}
			]
		},
		{
			"name" : "openSUSE 10.2",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-102-i586'>http://www.go-mono.com/download-stable/suse-102-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-102-x86_64'>http://www.go-mono.com/download-stable/suse-102-x86_64" + suseDownloadText2
			},
			{
				"name" : ppc,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-102-ppc'>http://www.go-mono.com/download-stable/suse-102-ppc" + suseDownloadText2
			}
			]
		},
		{
			"name" : "openSUSE 10.3",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-103-i586'>http://www.go-mono.com/download-stable/suse-103-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-103-x86_64'>http://www.go-mono.com/download-stable/suse-103-x86_64" + suseDownloadText2
			}
			]
		}
		]
	},

	{
		"name" : "SLES/SLED",
		"icon" : "sles.jpg",
		"dlicon" : "sles.jpg",
		"version" : [
		{
			"name" : "Suse Linux Enterprise Server 9 (SLES)",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-9-i586'>http://www.go-mono.com/download-stable/sles-9-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-9-x86_64'>http://www.go-mono.com/download-stable/sles-9-x86_64" + suseDownloadText2
			},
			{
				"name" : ppc,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-9-ppc'>http://www.go-mono.com/download-stable/sles-9-ppc" + suseDownloadText2
			},
			{
				"name" : ia64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-9-ia64'>http://www.go-mono.com/download-stable/sles-9-ia64" + suseDownloadText2
			},
			{
				"name" : s390,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-9-s390'>http://www.go-mono.com/download-stable/sles-9-s390" + suseDownloadText2
			},
			{
				"name" : s390x,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-9-s390x'>http://www.go-mono.com/download-stable/sles-9-s390x" + suseDownloadText2
			}
			]
		},
		{
			"name" : "Suse Linux Enterprise Server 10 (SLES)",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-i586'>http://www.go-mono.com/download-stable/suse-101-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-x86_64'>http://www.go-mono.com/download-stable/suse-101-x86_64" + suseDownloadText2
			},
			{
				"name" : ppc,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-ppc'>http://www.go-mono.com/download-stable/suse-101-ppc" + suseDownloadText2
			},
			{
				"name" : ia64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/sles-10-ia64'>http://www.go-mono.com/download-stable/sles-10-ia64" + suseDownloadText2
			}
			]
		},
		{
			"name" : "Suse Linux Enterprise Desktop 10 (SLED)",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-i586'>http://www.go-mono.com/download-stable/suse-101-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/suse-101-x86_64'>http://www.go-mono.com/download-stable/suse-101-x86_64" + suseDownloadText2
			}
			]
		},
		{
			"name" : "Novell Linux Desktop 9 (NLD)",
			"arch" : [
			{
				"name" : i586,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/nld-9-i586'>http://www.go-mono.com/download-stable/nld-9-i586" + suseDownloadText2
			},
			{
				"name" : x86_64,
				"desc" : "",
				"downloadText" : suseDownloadText1 + "http://www.go-mono.com/download-stable/nld-9-x86_64'>http://www.go-mono.com/download-stable/nld-9-x86_64" + suseDownloadText2
			}
			]
		}
		]
	},

	{
		"name" : "Windows",
		"icon" : "http://www.mono-project.com/files/0/00/Mono_icon_windows.gif",
		"dlicon" : "http://www.mono-project.com/files/0/00/Mono_icon_windows.gif",
		"version" : [
		{
			"name" : "Windows 2000, XP, 2003 and Vista",
			"arch" : [
			{
				"name" : "All",
				"desc" : "This version of Mono works on all versions of Windows 2000, XP, 2003 and Vista.",
				"downloadText" : "Mono for Windows, Gtk#, and XSP <ul><li><a href='ftp://www.go-mono.com/archive/1.2.6/windows-installer/4/mono-1.2.6-gtksharp-2.10.2-win32-4.exe'>Mono 1.2.6_4 Setup</a></ul>Only Gtk# for .NET: <ul><li><a href=' http://forge.novell.com/modules/xfmod/project/?gtks-inst4win'>SDK and Runtime</a></ul>Mono Migration Analyzer: <ul><li><a href='http://mono-project.com/MoMA'>See the Mono Migration Analyzer page</a></ul>"
			}
			]
		}
		]
	},

	{
		"name" : "Mac&nbsp;OS&nbsp;X",
		"icon" : "http://www.mono-project.com/files/b/bf/Mono_icon_mac.gif",
		"dlicon" : "http://www.mono-project.com/files/b/bf/Mono_icon_mac.gif",
		"version" : [
		{
			"name" : "Mac OS X Tiger (10.4) and Leopard (10.5)",
			"arch" : [
			{
				"name" : "All",
				"desc" : "This version of Mono works on Mac OS X Tiger (10.4) and Leopard (10.5).",
				"downloadText" : "Includes Mono, Cocoa#, installs in /Library/Frameworks:<ul><li><a href='ftp://www.go-mono.com/archive/1.2.6/macos-10-universal/4/MonoFramework-1.2.6_4.macos10.novell.universal.dmg'>Mono 1.2.6_4 Framework - Universal</a><li><a href='http://go-mono.com/sources/cocoa-sharp/cocoa-sharp-0.9.4.tar.bz2'>Cocoa# 0.9.4 source</a></ul>"
			}
			]
		}
		]
	},

	{
		"name" : "RedHat",
		"icon" : "http://www.mono-project.com/files/6/6e/Mono_icon_redhat.gif",
		"dlicon" : "http://www.mono-project.com/files/6/6e/Mono_icon_redhat.gif",
		"desc" : "This version of Mono works on RedHat Enterprise Linux 4 on x86 32bit (i586).",
		"version" : [
		{
			"name" : "RedHat Enterprise Linux 4",
			"arch" : [
			{
				"name" : i586,
				"desc" : "This version of Mono works on RedHat Enterprise Linux 4 on " + i586 + ".",
				"downloadText" : "The downloads are available <a href='http://www.go-mono.com/download-stable/rhel-4-i386'>here</a>."
			}
			]
		}
		]
	},

	{
		"name" : "Other&nbsp;Linux's",
		"icon" : "linux.jpg",
		"dlicon" : "linux.jpg",
		"version" : [
		{
			"name" : "Generic Linux",
			"arch" : [
			{
				"name" : i586,
				"desc" : "This version of Mono works on most generic Linux's on " + i586 + ".",
				"downloadText" : "For help with the installation, see: <a href='http://mono-project.com/InstallerInstructions'>Instructions to use the Installer</a>.<ul><li><a href='ftp://www.go-mono.com/archive/1.2.6/linux-installer/6/mono-1.2.6_6-installer.bin'>Mono 1.2.6_6 Installer</a></ul>"
			}
			]
		}
		]
	},

	{
		"name" : "Maemo",
		"icon" : "http://www.mono-project.com/files/a/aa/Maemo.gif",
		"dlicon" : "http://www.mono-project.com/files/a/aa/Maemo.gif",
		"version" : [
		{
			"name" : "Maemo",
			"arch" : [
			{
				"name" : "Nokia 770 and 800",
				"desc" : "This version of Mono works on Maemo for the Nokia 770 and 800.",
				"downloadText" : "For help with the installation, see <a href='http://mono-project.com/Maemo'>Mono for Nokia</a><ul><li><a href='http://go-mono.com/maemo/pool/bora/mono/mono.install'>Mono 1.2.5 Runtime Single Click Install</a><li><a href='http://go-mono.com/maemo/scratchbox-devkit-mono-1.2.3.1-2-i386.tar.gz'>Mono 1.2.3.1 Scratchbox developer kit</a></ul>"
			}
			]
		}
		]
	},

	{
		"name" : "Solaris",
		"icon" : "http://www.mono-project.com/files/2/2f/Mono_icon_solaris.gif",
		"dlicon" : "http://www.mono-project.com/files/2/2f/Mono_icon_solaris.gif",
		"version" : [
		{
			"name" : "Solaris 8",
			"arch" : [
			{
				"name" : "SPARC",
				"desc" : "This version of Mono works on Solaris 8 on SPARC.",
				"downloadText" : "<a href='http://mono-project.com/SolarisInstructions'>Solaris package instructions<ul><li><a href='ftp://www.go-mono.com/archive/1.2.4/sunos-8-sparc/4/mono-1.2.4_4.sunos8.novell.sparc.pkg.gz'>Mono 1.2.4_4 Package</a></ul>"
			}
			]
		}
		]
	}

	]
};
