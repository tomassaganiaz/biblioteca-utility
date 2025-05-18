from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportePDF:
    def _init_(self, biblioteca):
        self.biblioteca = biblioteca

    def generar_pdf(self, nombre_archivo):
        c = canvas.Canvas(nombre_archivo, pagesize=letter)
        c.drawString(100, 750, "📚 Reporte de Préstamos - Biblioteca")
        
        y = 730
        for fecha, usuario, libro in self.biblioteca.historial_prestamos:
            c.drawString(100, y, f"{fecha} | {usuario} | {libro}")
            y -= 20
        
        c.save()
        return f'✅ Reporte exportado como "{nombre_archivo}".'