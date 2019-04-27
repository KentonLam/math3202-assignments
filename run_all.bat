@ECHO OFF
pushd
cd %~dp0 

call %HOME%\Anaconda3\Scripts\activate.bat

set a=5
echo Running communication %a%
python assignment_model.py %a% > comm_%a%_output.md

set a=6
echo Running communication %a%
python assignment_model.py %a% > comm_%a%_output.md

set a=7
echo Running communication %a%
python assignment_model.py %a% > comm_%a%_output.md

set a=8
echo Running communication %a%
python assignment_model.py %a% > comm_%a%_output.md

set a=9
echo Running communication %a%
python assignment_model.py %a% > comm_%a%_output.md

popd