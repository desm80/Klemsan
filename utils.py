import os


def clear_folder(folder):
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))


def xls_to_xlsx_converter(files):
    import jpype
    import asposecells
    jpype.startJVM()
    from asposecells.api import Workbook

    # Load XLS file
    for file in files:
        workbook = Workbook(file);
        cut = file.split('.xls')[0]
        cut = cut + '.xlsx'
        # Save as XLSX
        workbook.save(cut);

    # Shutdown JVM
    jpype.shutdownJVM()
