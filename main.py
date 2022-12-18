import os
import click
from automato.mealyAutomato import mealyAutomato


@click.command()
@click.option(
    '--path',
    '-p',
    help='Caminho para o arquivo de execução.',
    required=True
)
def main(path):
    if not os.path.isfile(path):
        print('O caminho {} não existe'.format(path))
        return

    file = open(path, "r")
    try:
        print(mealyAutomato.get_output_from_string(file.read()))
    except:
        print('Não foi possível obter a lista de tokens...')

    file.close()


if __name__ == "__main__":
    main()
