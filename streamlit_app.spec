# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

from PyInstaller.utils.hooks import copy_metadata, collect_data_files

datas = []
datas += copy_metadata('streamlit')
datas += copy_metadata('pandas')
datas += copy_metadata('openpyxl')
datas += copy_metadata('altair')
datas += copy_metadata('numpy')
datas += copy_metadata('pytz')

# Add Streamlit static files
datas += collect_data_files('streamlit')

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas + [('app', 'app'), ('app/.streamlit', '.streamlit')],
    hiddenimports=[
        'streamlit',
        'streamlit.web.cli',
        'streamlit.web.server',
        'streamlit.web.bootstrap',
        'streamlit.runtime',
        'streamlit.runtime.scriptrunner',
        'streamlit.runtime.scriptrunner.magic_funcs',
        'streamlit.runtime.caching',
        'streamlit.runtime.state',
        'streamlit.runtime.legacy_caching',
        'streamlit.web.server.server',
        'streamlit.web.server.server_util',
        'streamlit.components.v1',
        'pandas',
        'openpyxl',
        'app.consolidator',
        'webbrowser',
        'threading',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='libro-diario-converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
