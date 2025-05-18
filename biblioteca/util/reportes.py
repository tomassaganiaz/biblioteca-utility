from model.reporte_biblioteca import ReporteBiblioteca
from model.reporte_pdf import ReportePDF

class Reportes:
    def _init_(self, biblioteca):
        self.biblioteca = biblioteca
        self.reporte_csv = ReporteBiblioteca(biblioteca)
        self.reporte_pdf = ReportePDF(biblioteca)

    def generar_reporte(self, tipo, nombre_archivo):
        if tipo.lower() == "csv":
            return self.reporte_csv.exportar_csv(nombre_archivo)
        elif tipo.lower() == "pdf":
            return self.reporte_pdf.generar_pdf(nombre_archivo)
        else:
            return "Tipo de reporte no válido. Usa 'csv' o 'pdf'."