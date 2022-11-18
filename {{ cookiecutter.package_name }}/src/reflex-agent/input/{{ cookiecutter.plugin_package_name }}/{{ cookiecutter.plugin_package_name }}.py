from typing import Dict, Any

from reflexsoar_agent.input.base import BaseInput, InputTypes
from reflexsoar_agent.core.logging import logger
        

class {{ cookiecutter.plugin_class_name }}Input(BaseInput):
    """Defines the {{ cookiecutter.plugin_package_name }} input"""

    alias = "{{ cookiecutter.plugin_package_name }}"
    config_fields = []

    def __init__(self, config: Dict[Any, Any], input_type: str = InputTypes.POLL):
        """Initializes the {{ cookiecutter.plugin_name }} input"""

        super().__init__(input_type, config)
        
    def main(self):
        """Main method for the {{ cookiecutter.plugin_name }} input"""

        logger.info("{{ cookiecutter.plugin_name }} input started")


if __name__ == "__main__":
    {{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_class_name }}Input()
    {{ cookiecutter.plugin_name }}.main()
