# -*- mode: python -*-

block_cipher = None

a = Analysis(
    # when invoking pyinstaller from the project root,
    # this gets invoked from the directory of the spec file,
    # i.e. ./.github/pyinstaller
    ['../../floss/main.py'],
             pathex=['floss'],
             binaries=None,
             datas=None,
             hiddenimports=[
                "viv_utils",

                # vivisect does manual/runtime importing of its modules,
                # so declare the things that could be imported here.
                "pycparser",
                "vivisect",
                "vivisect.analysis",
                "vivisect.analysis.amd64",
                "vivisect.analysis.amd64",
                "vivisect.analysis.amd64.emulation",
                "vivisect.analysis.amd64.golang",
                "vivisect.analysis.crypto",
                "vivisect.analysis.crypto",
                "vivisect.analysis.crypto.constants",
                "vivisect.analysis.elf",
                "vivisect.analysis.elf",
                "vivisect.analysis.elf.elfplt",
                "vivisect.analysis.elf.libc_start_main",
                "vivisect.analysis.generic",
                "vivisect.analysis.generic",
                "vivisect.analysis.generic.codeblocks",
                "vivisect.analysis.generic.emucode",
                "vivisect.analysis.generic.entrypoints",
                "vivisect.analysis.generic.funcentries",
                "vivisect.analysis.generic.impapi",
                "vivisect.analysis.generic.mkpointers",
                "vivisect.analysis.generic.pointers",
                "vivisect.analysis.generic.pointertables",
                "vivisect.analysis.generic.relocations",
                "vivisect.analysis.generic.strconst",
                "vivisect.analysis.generic.switchcase",
                "vivisect.analysis.generic.thunks",
                "vivisect.analysis.i386",
                "vivisect.analysis.i386",
                "vivisect.analysis.i386.calling",
                "vivisect.analysis.i386.golang",
                "vivisect.analysis.i386.importcalls",
                "vivisect.analysis.i386.instrhook",
                "vivisect.analysis.i386.thunk_bx",
                "vivisect.analysis.ms",
                "vivisect.analysis.ms",
                "vivisect.analysis.ms.hotpatch",
                "vivisect.analysis.ms.localhints",
                "vivisect.analysis.ms.msvc",
                "vivisect.analysis.ms.msvcfunc",
                "vivisect.analysis.ms.vftables",
                "vivisect.analysis.pe",
                "vivisect.impapi.posix.amd64",
                "vivisect.impapi.posix.i386",
                "vivisect.impapi.windows",
                "vivisect.impapi.windows.amd64",
                "vivisect.impapi.windows.i386",
                "vivisect.impapi.winkern.i386",
                "vivisect.impapi.winkern.amd64",
                "vivisect.parsers.blob",
                "vivisect.parsers.elf",
                "vivisect.parsers.ihex",
                "vivisect.parsers.macho",
                "vivisect.parsers.pe",
                "vivisect.parsers.utils",
                "vivisect.storage",
                "vivisect.storage.basicfile",
                "vstruct.constants",
                "vstruct.constants.ntstatus",
                "vstruct.defs",
                "vstruct.defs.arm7",
                "vstruct.defs.bmp",
                "vstruct.defs.dns",
                "vstruct.defs.elf",
                "vstruct.defs.gif",
                "vstruct.defs.ihex",
                "vstruct.defs.inet",
                "vstruct.defs.java",
                "vstruct.defs.kdcom",
                "vstruct.defs.macho",
                "vstruct.defs.macho.const",
                "vstruct.defs.macho.fat",
                "vstruct.defs.macho.loader",
                "vstruct.defs.macho.stabs",
                "vstruct.defs.minidump",
                "vstruct.defs.pcap",
                "vstruct.defs.pe",
                "vstruct.defs.pptp",
                "vstruct.defs.rar",
                "vstruct.defs.swf",
                "vstruct.defs.win32",
                "vstruct.defs.windows",
                "vstruct.defs.windows.win_5_1_i386",
                "vstruct.defs.windows.win_5_1_i386.ntdll",
                "vstruct.defs.windows.win_5_1_i386.ntoskrnl",
                "vstruct.defs.windows.win_5_1_i386.win32k",
                "vstruct.defs.windows.win_5_2_i386",
                "vstruct.defs.windows.win_5_2_i386.ntdll",
                "vstruct.defs.windows.win_5_2_i386.ntoskrnl",
                "vstruct.defs.windows.win_5_2_i386.win32k",
                "vstruct.defs.windows.win_6_1_amd64",
                "vstruct.defs.windows.win_6_1_amd64.ntdll",
                "vstruct.defs.windows.win_6_1_amd64.ntoskrnl",
                "vstruct.defs.windows.win_6_1_amd64.win32k",
                "vstruct.defs.windows.win_6_1_i386",
                "vstruct.defs.windows.win_6_1_i386.ntdll",
                "vstruct.defs.windows.win_6_1_i386.ntoskrnl",
                "vstruct.defs.windows.win_6_1_i386.win32k",
                "vstruct.defs.windows.win_6_1_wow64",
                "vstruct.defs.windows.win_6_1_wow64.ntdll",
                "vstruct.defs.windows.win_6_2_amd64",
                "vstruct.defs.windows.win_6_2_amd64.ntdll",
                "vstruct.defs.windows.win_6_2_amd64.ntoskrnl",
                "vstruct.defs.windows.win_6_2_amd64.win32k",
                "vstruct.defs.windows.win_6_2_i386",
                "vstruct.defs.windows.win_6_2_i386.ntdll",
                "vstruct.defs.windows.win_6_2_i386.ntoskrnl",
                "vstruct.defs.windows.win_6_2_i386.win32k",
                "vstruct.defs.windows.win_6_2_wow64",
                "vstruct.defs.windows.win_6_2_wow64.ntdll",
                "vstruct.defs.windows.win_6_3_amd64",
                "vstruct.defs.windows.win_6_3_amd64.ntdll",
                "vstruct.defs.windows.win_6_3_amd64.ntoskrnl",
                "vstruct.defs.windows.win_6_3_i386",
                "vstruct.defs.windows.win_6_3_i386.ntdll",
                "vstruct.defs.windows.win_6_3_i386.ntoskrnl",
                "vstruct.defs.windows.win_6_3_wow64",
                "vstruct.defs.windows.win_6_3_wow64.ntdll",
             ],
             hookspath=None,
             runtime_hooks=None,
             excludes=["tkinter", "_tkinter", "Tkinter"],
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)

a.binaries = a.binaries - TOC([
 ('sqlite3.dll', None, None),
 ('tcl85.dll', None, None),
 ('tk85.dll', None, None),
 ('_sqlite3', None, None),
 ('_ssl', None, None),
 ('_tkinter', None, None)])

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          exclude_binaries=False,
          name='floss',
          # when invoking pyinstaller from the project root,
          # this gets invoked from the directory of the spec file,
          # i.e. ./.github/pyinstaller
          icon='../../resources/icon.ico',
          debug=False,
          strip=None,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='floss-dat')

