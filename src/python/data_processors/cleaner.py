class DataCleaner:
    def __init__(self):
        pass

    def clean_data(self, data):
        cleaned_data = []
        for item in data:
            if item:  # Example condition to filter out empty items
                cleaned_data.append(item.strip())
        return cleaned_data

    def remove_duplicates(self, data):
        return list(set(data))  # Removes duplicates by converting to a set and back to a list