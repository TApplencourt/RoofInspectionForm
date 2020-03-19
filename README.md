# RoofInspectionForm

## How to use 

```
./run.sh  <bin> <args>
```

## Restriction to comply

`<bin>` should print the data on STDOUT following the syntax `advisor__{name} {value}`
When `{name}` is one of this row provided by `{ADVISOR}/pythonapi/examples/survey_gpu.py`.

For example:
```
advisor__gpu_compute_performance_gflops  33.863
```
