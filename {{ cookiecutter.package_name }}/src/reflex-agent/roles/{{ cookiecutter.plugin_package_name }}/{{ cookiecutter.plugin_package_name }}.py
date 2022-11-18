from reflexsoar_agent.role.base import BaseRole
from reflexsoar_agent.core.logging import logger
        

class {{ cookiecutter.plugin_class_name }}Role(BaseRole):
    """Defines the SysBeat role.  SysBeat is responsible for providing a 
    hosted repository of sysmon and beat configs that remove machines can
    subscribe to and download from.
    """

    alias = "{{ cookiecutter.plugin_package_name }}"
    config_fields = []

    def __init__(self, *args, **kwargs):
        """Initializes the {{ cookiecutter.plugin_name }} role"""

        super().__init__({}, [], *args, **kwargs)
        
    def main(self):
        """Main method for the {{ cookiecutter.plugin_name }} role"""

        logger.info("{{ cookiecutter.plugin_name }} role started")


if __name__ == "__main__":
    {{ cookiecutter.plugin_name }} = {{ cookiecutter.plugin_class_name }}()
    {{ cookiecutter.plugin_name }}.main()
