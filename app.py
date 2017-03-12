import click
import project

@click.group()
def cli():
    pass

@click.command()
@click.option('--template')
@click.option('--project-name')
@click.option('--git-url')
def new(project_name, template, git_url):
    project.new(project_name, template, git_url)

cli.add_command(new)

@click.command()
def setup():
    print("running setup steps...")

cli.add_command(setup)


@click.command()
def lint():
    print("running lint steps...")

cli.add_command(lint)


@click.command()
def build():
    print("running build steps...")
    project.build(project_name, template, git_url)

cli.add_command(build)


@click.command()
def unit_test():
    print("running unit-test steps...")

cli.add_command(unit_test)

@click.command()
def package():
    print("running package steps...")

cli.add_command(package)

@click.command()
def publish():
    print("running publish steps...")

cli.add_command(publish)


@click.command()
@click.option('--environment')
def deploy():
    print("running deploy steps...")

cli.add_command(deploy)


@click.command()
@click.option('--environment')
def acceptance_tests():
    print("running acceptance_tests steps...")

cli.add_command(acceptance_tests)

@click.command()
@click.option('--environment')
def cleanup():
    print("running cleanup steps...")

cli.add_command(cleanup)


if __name__ == '__main__':
    cli()