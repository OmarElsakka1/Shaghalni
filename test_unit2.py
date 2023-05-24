import pytest
from werkzeug.datastructures import FileStorage
from website.models import  Job, User, JobApplication
from website.file_manager import FileManager
from pathlib import Path



@pytest.fixture
def file_manager():
    return FileManager()


@pytest.fixture
def sample_file():
    return FileStorage(filename='test.jpg')


@pytest.fixture
def sample_owner():
    return Job(id=123)  # Replace with appropriate owner object


def test_is_image_returns_true_for_supported_extensions(file_manager):
    assert file_manager.IsImage(FileStorage(filename='image.png'))
    assert file_manager.IsImage(FileStorage(filename='image.jpg'))
    assert file_manager.IsImage(FileStorage(filename='image.jpeg'))


def test_is_image_returns_false_for_unsupported_extensions(file_manager):
    assert not file_manager.IsImage(FileStorage(filename='image.txt'))
    assert not file_manager.IsImage(FileStorage(filename='image.pdf'))


def test_save_file_returns_save_location_for_job_owner(file_manager, sample_file, sample_owner):
    save_loc = file_manager.SaveFile(sample_file, sample_owner)
    assert Path.samefile(Path(save_loc), Path('instance/Images/Jobs/123.jpg'))  # Use Path.samefile to compare paths, not Path.isequalt


def test_save_file_returns_save_location_for_user_owner(file_manager, sample_file, sample_owner):
    sample_owner = User(id=456)  # Replace with appropriate owner object
    save_loc = file_manager.SaveFile(sample_file, sample_owner)
    assert Path.samefile(Path(save_loc), Path('instance/Images/Users/456.jpg'))  # Use Path.samefile to compare paths, not Path.isequalt





def test_save_file_returns_none_for_unknown_owner(file_manager, sample_file):
    save_loc = file_manager.SaveFile(sample_file, None)
    assert save_loc is None