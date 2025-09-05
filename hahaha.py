import subprocess
# import streamlit as st
# import time

# st.title("Progess")

# progress_bar = st.progress(0)
# for i in range(100):
#     # Update the progress bar's value
#     progress_bar.progress(i + 1)
#     time.sleep(0.01)

# #st.success('Task complete!')    

#  "rsync -av --progress cts@192.168.15.201:/opt/android/atv14/cts/android-cts/results/latest/test_result.html /var/www/html/test/"
#  "rsync -av --progress cts@192.168.15.201:/opt/android/atv14/cts/android-cts/results/latest/test_result_failures_suite.html /var/www/html/test/"
#  "rsync -av --progress cts@192.168.15.201:/opt/android/atv14/cts/android-cts/results/latest/compatibility_result.css /var/www/html/test/"
#  "rsync -av --progress cts@192.168.15.201:/opt/android/atv14/cts/android-cts/results/latest/logo.png /var/www/html/test/"

vph1path1 = "/opt/android/atv14/cts/android-cts/results/latest/test_result.html /var/www/html/test/"
# vpathsource2 = "/opt/android/atv14/cts/android-cts/results/latest/test_result_failures_suite.html /var/www/html/test/"
# vpathsource3 = "/opt/android/atv14/cts/android-cts/results/latest/compatibility_result.css /var/www/html/test/"
# vpathsuorce4 = "/opt/android/atv14/cts/android-cts/results/latest/logo.png /var/www/html/test/"

# vpathdest1 = "/var/www/html/test/"
vvmpath1 = "/opt"
# vpathdest2 = "/var/www/html/test/"
# vpathdest3 = "/var/www/html/test/"
# vpathdest4 = "/var/www/html/test/"

vcommand = "/usr/bin/rsync -av"

# server ph3
vipsource = "192.168.15.207"
vuser = "cts"
vdoublepoint = ":"
varrouba = "@"

# server vm
vipdest = "192.168.15.156"

command = [vcommand, vuser, varrouba, vipsource, vdoublepoint, vph1path1, vvmpath1]

try:
    result = subprocess.run(
        command,
        check=True,  # Raises an exception if the command fails
        capture_output=True, # Captures stdout and stderr
        text=True # Decodes output as text
    )
    print("rsync completed successfully.")
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)

except subprocess.CalledProcessError as e:
    print("rsync failed.")
    print("Return code:", e.returncode)
    print("Stdout:", e.stdout)
    print("Stderr:", e.stderr)








