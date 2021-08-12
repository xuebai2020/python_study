import pytest
import yaml

@pytest.mark.parametrize("env", yaml.safe_load(open("./data.yml")))
class Test:
    def test_data(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
        elif "dev" in env:
            print("这是开发环境")
