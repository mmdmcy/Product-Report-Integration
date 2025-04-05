class DataTransformer:
    def transform_data(self, data):
        """
        Transforms the input data into the required format.
        
        Parameters:
            data (list): The input data to be transformed.
        
        Returns:
            list: The transformed data.
        """
        # Example transformation logic
        transformed_data = [self.format_data(item) for item in data]
        return transformed_data

    def format_data(self, item):
        """
        Formats a single data item.
        
        Parameters:
            item (dict): The data item to be formatted.
        
        Returns:
            dict: The formatted data item.
        """
        # Example formatting logic
        formatted_item = {
            'id': item.get('id'),
            'name': item.get('name').strip().title(),
            'value': float(item.get('value', 0))
        }
        return formatted_item