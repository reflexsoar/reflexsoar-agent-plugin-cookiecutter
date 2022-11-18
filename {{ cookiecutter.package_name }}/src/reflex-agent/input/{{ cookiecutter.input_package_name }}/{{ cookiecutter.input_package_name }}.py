from reflexsoar_agent.input.base import BaseInput
from reflexsoar_agent.core.logging import logger
        

class {{ cookiecutter.input_class_name }}(BaseInput):
    """Defines the {{ cookiecutter.input_package_name }} input"""

    alias = "{{ cookiecutter.input_package_name }}"
    config_fields = []

    def __init__(self, *args, **kwargs):
        """Initializes the {{ cookiecutter.input_name }} role"""

        super().__init__({}, [], *args, **kwargs)
        
    def main(self):
        """Main method for the {{ cookiecutter.input_name }} input"""

        logger.info("{{ cookiecutter.input_name }} input started")


if __name__ == "__main__":
    {{ cookiecutter.input_name }} = {{ cookiecutter.input_class_name }}()
    {{ cookiecutter.input_name }}.main()
