import os


class ImporterCSV:
    def __init__(self, csv_folder_name):
        self.csv_folder_name = csv_folder_name

    def get_attributes(self):
        fn = os.path.join(self.csv_folder_name, "")

def import_from_csv_folder(container, csv_folder_name):
    """
    Import container data from CSVs in a folder.

    csv_folder_name: string
        Name of folder

    Examples
    ----------
    >>> container.import_from_csv_folder(csv_folder_name)
    """

    print('working')