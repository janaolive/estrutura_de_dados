from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    current_path = None
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            current_path = instance.search(item)
    if current_path is None:
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(txt_importer(path_file)),
            "linhas_do_arquivo": txt_importer(path_file)
        }
        instance.enqueue(data)
        sys.stdout.write(f"{data}")


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance):
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")
    sys.stdout.write("Não há elementos\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        sys.stdout.write(f"{instance.search(position)}\n")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
