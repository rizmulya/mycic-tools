from datetime import date as d


def dn():
    days = ["Senin", "Selasa", "Rabu",
                 "Kamis", "Jumat", "Sabtu", "Minggu"]
    months = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    date_today = d.today()
    day = days[date_today.weekday()]
    date = date_today.day
    month = months[date_today.month - 1]
    year = date_today.year
    format_date = f"{day}, {date:02d} {month} {year}"
    return format_date
