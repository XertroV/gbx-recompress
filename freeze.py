from py2exe import freeze
freeze(
    console=['recompress.py'],
    windows=[],
    data_files=None,
    zipfile=None,
    options={"includes": ["pathlib", "struct", "binascii", "logging", "click", "lzo", "pygbx"]},
    version_info={}
)
