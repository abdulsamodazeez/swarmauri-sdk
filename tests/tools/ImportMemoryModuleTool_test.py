import pytest
from swarmauri.standard.tools.concrete.ImportMemoryModuleTool import ImportMemoryModuleTool as Tool

@pytest.mark.unit
def test_ubc_resource():
    def test():
        tool = Tool()
        assert tool.resource == 'Tool'
    test()

@pytest.mark.unit
def test_initialization():
    def test():
        tool = Tool()
        assert type(tool.swm_path) == str
        assert type(tool.id) == str
    test()

@pytest.mark.unit
def test_call():
    def test():
        tool = Tool()
        name_of_new_module = 'test_module'
        code_snippet = "def example_function():" \
            "\t\treturn 'This function is imported from memory.'"

        dot_separated_package_page = "test_package"
        result = tool(name_of_new_module,
                                     code_snippet,
                                     dot_separated_package_page)

        
        from test_package.test_module import example_function
        assert example_function() == 'This function is imported from memory.'
    
    test()