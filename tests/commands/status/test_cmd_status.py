from click.testing import CliRunner
from complex.cli import pass_environment
from complex.cli import cli

def test_complex_init():
  runner = CliRunner()
  result = runner.invoke(cli, ['status', '--help'])
  assert result.exit_code == 0