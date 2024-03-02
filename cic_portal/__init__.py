from dotenv import dotenv_values

env = {
    **dotenv_values(".env"),
    'BASE_URL': "https://my.cic.ac.id/portal/mahasiswa",
    'BASE_URL2': "https://my.cic.ac.id/portal/sipandai",
    'LOGIN_URL': "?mod=loginact",
    'DASHBOARD_URL': "?mod=student&act=dashboard",
    'MATKUL_URL': "?mod=sipandai&act=dashboardmahasiswa",
    'LOGOUT_URL': "controllers/logout.php",
    'COURSE_URL': "?mod=student&act=course",
}

head = {
    'User-Agent': env["USER_AGENT"]
}
