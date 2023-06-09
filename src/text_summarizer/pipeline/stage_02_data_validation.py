from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.components.data_validation import DataValiadtion
from text_summarizer.longging import logger


class DatavalidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.download_file()
        data_validation.extract_zip_file()