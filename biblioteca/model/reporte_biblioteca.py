import pandas as pd

class ReporteBiblioteca:
    def _init_(self, biblioteca):
        self.biblioteca = biblioteca

    def exportar_csv(self, nombre_archivo):
        data = [{"Fecha": fecha, "Usuario": usuario, "Libro": libro} for fecha, usuario, libro in self.biblioteca.historial_prestamos]
        df = pd.DataFrame(data)
        df.to_csv(nombre_archivo, index=False)
        return f'✅ Reporte exportado como "{nombre_archivo}".'