from dataclasses import dataclass

@dataclass
class DataIngestonAtrifact:
    train_file_path:str
    test_file_path:str
    
@dataclass
class DataValidationAtrifact:
    validation_status:bool
    message:str
    drift_report_file_path:str