from reflexsoar_agent.input.base import BaseInput
from reflexsoar_agent.core.logging import logger
        

class {{ cookiecutter.plugin_class_name }}(BaseInput):
    """Defines the {{ cookiecutter.plugin_package_name }} input"""

    alias = "{{ cookiecutter.plugin_package_name }}"
    config_fields = []

    def __init__(self, *args, **kwargs):
        """Initializes the {{ cookiecutter.plugin_name }} role"""

        super().__init__({}, [], *args, **kwargs)
        
    def main(self):
        """Main method for the {{ cookiecutter.plugin_name }} input"""

        logger.info("{{ cookiecutter.plugin_name }} input started")


if __name__ == "__main__":
    {{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_class_name }}()
    {{ cookiecutter.plugin_name }}.main()
