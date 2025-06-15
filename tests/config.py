from pydantic import (
    BaseModel,
)


class Service(BaseModel):
    URL: str = "https://makarovartem.github.io/frontend-avito-tech-test-assignment"


class TestCards(BaseModel):
    PARENT_SELECTOR: str = "ul.ant-list-items > li"
    CHILD_SELECTOR: str = "h2.ant-typography"


class TestDisplayCount(BaseModel):
    PARENT_SELECTOR: str = "ul.ant-list-items > li"

class TestFilterByCategory(BaseModel):
    SELECTION_ITEM: str = ".ant-select-selection-item"
    SELECTION_DROPDOWN: str = ".ant-select-dropdown"
    SELECTION_LIST: str = "ul.ant-list-items > li"

class TestFilterByPlatform(BaseModel):
    SELECTION_LIST: str = "ul.ant-list-items > li"
    SELECTION_ITEM: str = ".ant-select-selection-item"
    SELECTION_DROPDOWN: str = ".ant-select-dropdown"

class TestPagination(BaseModel):
    SELECTION_LIST: str = "ul.ant-list-items > li"
    SELECTION_ITEM: str = "li.ant-pagination-item-active"

class TestSortBy(BaseModel):
    SELECTION_ITEM: str = ".ant-select-selection-item"
    SELECTION_DROPDOWN: str = ".ant-select-dropdown"
    SELECTION_LIST: str = "ul.ant-list-items > li"

class Config(BaseModel):
    srv: Service = Service()
    cards: TestCards = TestCards()
    display_cards : TestDisplayCount = TestDisplayCount()
    filter_by_category: TestFilterByCategory = TestFilterByCategory()
    filter_by_platform: TestFilterByPlatform = TestFilterByPlatform()
    pagination: TestPagination = TestPagination()
    sort_by: TestSortBy = TestSortBy()


def get() -> Config:
    return Config()