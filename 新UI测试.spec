# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['新UI测试.py'],
    pathex=[],
    binaries=[],
    datas=[('c:\\users\\rjcsyb2\\appdata\\roaming\\python\\python38\\site-packages\\customtkinter', 'customtkinter'), ('c:\\users\\rjcsyb2\\appdata\\roaming\\python\\python38\\site-packages\\ddddocr', 'ddddocr'), ('C:\\Users\\rjcsyb2\\Desktop\\workcard-master\\网关车联\\test_images', 'test_images')],
    hiddenimports=[],
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
    name='新UI测试',
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
    icon=['C:\\Users\\rjcsyb2\\Desktop\\workcard-master\\网关车联\\test_images\\cache.ico'],
)
