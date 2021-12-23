from reportlab.lib.pagesizes import A4, A3, landscape

sizes = (
    ('A3L', 420, 297, landscape(A3)), 
    ('A3', 297, 420, A3), 
    ('A4L', 297, 210, landscape(A4)), 
    ('A4', 210, 297, A4),
    )