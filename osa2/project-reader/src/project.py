class Project:
    def __init__(self, name, description, dependencies, dev_dependencies,
                 license_name, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license_name = license_name
        self.authors = authors

    def _stringify_list(self, items):
        if len(items) == 0:
            return "\n-"

        return "".join(f"\n- {item}" for item in items)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license_name or '-'}"
            f"\n\nAuthors:{self._stringify_list(self.authors)}"
            f"\n\nDependencies:{self._stringify_list(self.dependencies)}"
            f"\n\nDevelopment dependencies:"
            f"{self._stringify_list(self.dev_dependencies)}"
        )