#!/bin/sh
# 사용법
usage()
{
  echo "$0 -c FILE_NAME"
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
echo "CONFIG_NAME=${CONFIG_NAME}"


#if [ "$CONFIG_NAME" != "" ]; then
#  sed -i 's/CELERY_CONFIG_MODULE="django_celery_test.celery"/CELERY_CONFIG_MODULE="django_celery_test.'"$CONFIG_NAME"'"/g' celeryd
#fi

cp generic_celeryd /etc/init.d/celeryd && sudo chmod 755 /etc/init.d/celeryd && sudo chown root:root /etc/init.d/celeryd