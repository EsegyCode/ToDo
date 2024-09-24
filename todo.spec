# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['todo.py'],
    pathex=[],
    binaries=[],
    datas=[('image/scrr.png', 'img'), ('image/top.png', 'img'), ('image/doc.png', 'img'), ('image/task.png', 'img'), ('image/trash.png', 'img'), ('image', 'image')],
    hiddenimports=['tkinter', 'os', 'sys'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='todo',
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
