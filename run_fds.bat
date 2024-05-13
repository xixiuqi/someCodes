@echo off
for /r %%i in (*) do (
    if /i "%%~ai"=="d" (
        pushd "%%i"
        fds output.fds
        popd
    )
)
