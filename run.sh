export ADVIXE_EXPERIMENTAL=gpu-profiling
export PRJ=./
export SRC=./

advixe-cl --collect=roofline --enable-gpu-profiling --project-dir=$PRJ --search-dir src:r=$SRC -- ./"$@"
advixe-cl --report=roofline --gpu --project-dir=$PRJ --report-output=${PRJ}/roofline.html
advixe-python ${ADVISOR}/pythonapi/examples/survey_gpu.py $PRJ > ./advisor_raw_data.txt

./"$@" > application_raw_data.txt

./compare_number.py application_raw_data.txt advisor_raw_data.txt
