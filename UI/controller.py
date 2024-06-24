import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_rete(self, e):
        anno = self._view.dd_anno.value
        if anno is None:
            self._view.create_alert("Selezionare un Anno")
            return
        grafo = self._model.creaGrafo(int(anno))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        dizio=self._model.analisi()
        for nodo in dizio.keys():
            self._view.txt_result.controls.append(ft.Text(f"I vicini del nodo {nodo} sono:"))
            for (elemento,peso) in dizio[nodo]:
                self._view.txt_result.controls.append(ft.Text(f"{elemento} con una distanza di {peso} km"))
        self._view.update_page()

    def fillDD(self):
        anni=self._model.getAnni
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(
                text=anno))
