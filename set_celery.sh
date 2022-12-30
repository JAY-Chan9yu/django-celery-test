#!/bin/sh
# 사용법
usage()
{
  echo "$0 -c CONFIG_NAME"
  echo "<options>"
  echo "    -c     : celery config 파일명"
  echo "<exit code>"
  echo "    0: Success."
  echo "    1: Failure."
  exit 1
}

#실행 옵션 설정
while getopts c:h opts; do
    case $opts in
    c) CONFIG_NAME=$OPTARG
            ;;
    h) usage
            ;;
    \?) usage
            ;;
    esac
done

#실행 옵션 확인
if [ -z "$CONFIG_NAME" ]; then
    echo "CONFIG_NAME is not empty"
else
  echo "cp ${CONFIG_NAME}.service"
  cp ./celery_conf/"${CONFIG_NAME}".service /etc/systemd/system/"${CONFIG_NAME}".service
fi
