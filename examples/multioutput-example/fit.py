from igel import IgelModel

"""
The goal of igel is to use ML without writing code. Therefore, the right and simplest way to use igel is from terminal.
You can run ` igel fit -dp path_to_dataset -yml path_to_yaml_file`.

Alternatively, you can write code if you want. This example below demonstrates how to use igel if you want to write code.

"""
mock_fit_params = {'data_path': './linnerud.csv',
                   'yaml_path': './multioutput.yaml',
                   'cmd': 'fit'}

IgelModel(**mock_fit_params).fit()
