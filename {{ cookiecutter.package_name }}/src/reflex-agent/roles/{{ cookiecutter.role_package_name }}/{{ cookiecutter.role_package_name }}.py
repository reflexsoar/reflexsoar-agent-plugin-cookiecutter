from reflexsoar_agent.role.base import BaseRole
from reflexsoar_agent.core.logging import logger
        

class {{ cookiecutter.role_class_name }}(BaseRole):
    """Defines the SysBeat role.  SysBeat is responsible for providing a 
    hosted repository of sysmon and beat configs that remove machines can
    subscribe to and download from.
    """

    alias = "{{ role_package_name }}"
    config_fields = []

    def __init__(self, *args, **kwargs):
        """Initializes the {{ cookiecutter.role_name }} role"""

        super().__init__({}, [], *args, **kwargs)
        
    def main(self):
        """Main method for the {{ cookiecutter.role_name }} role"""

        logger.info("{{ cookiecutter.role_name }} role started")


if __name__ == "__main__":
    {{ cookiecutter.role_name }} = {{ cookiecutter.role_class_name }}()
    {{ cookiecutter.role_name }}.main()
