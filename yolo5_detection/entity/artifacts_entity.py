from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_zip_file_path : str
    data_store_path : str


@dataclass
class DataValidationArtifact:
    validation_status : bool 