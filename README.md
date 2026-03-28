# SF-ONE TurtleBot 연동 테스트

## 프로젝트 개요
본 저장소는 SF-ONE 팀 프로젝트에서  
터틀봇 카메라 연동, 영상 출력, YOLO 객체 인식 적용을 테스트하고 검증하기 위해 정리한 코드입니다.

학습된 모델을 실제 TurtleBot 환경에 연결하고,  
카메라 입력과 객체 인식이 정상적으로 동작하는지 확인하는 과정을 기록했습니다.

## 사용 기술
- Python
- ROS2
- OpenCV
- YOLOv8
- TurtleBot3

## 담당 역할
- TurtleBot 카메라 연동 테스트
- ROS2 환경에서 영상 출력 및 지연 확인
- YOLO 가중치 파일 적용 및 객체 인식 테스트
- 시스템 실행 및 동작 검증
- 실제 환경에서 발생하는 문제 확인 및 피드백 정리

## 주요 파일
- `camera_view_test.py` : TurtleBot 카메라 영상 출력 테스트
- `turtlebot_yolo_test.py` : YOLO 객체 인식 연동 테스트

## 테스트 내용
- 카메라 토픽(`/image_raw`) 수신 확인
- OpenCV를 이용한 실시간 영상 출력
- YOLO 가중치 파일 적용 및 객체 인식 결과 확인
- ROS2 패키지 빌드 및 실행 검증

## 한 줄 정리
TurtleBot 환경에서 카메라와 YOLO 객체 인식을 실제로 연결하고 검증한 테스트용 저장소입니다.
