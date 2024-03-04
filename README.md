# super-resolution
이 레포지토리는 Fly Ai 프로젝트 "AI 도슨트 서비스 : Acent"에서 upscale 기능을 구현한 것입니다.

### 기능 목적 
- 사용자 input 이미지에 대해서 흔들림이나, 저화질의 이미지를 upscale하여, 이후 따라오는 이미지 처리 기능에 퀄리티를 향상시키기 위함.(화질 개선 및 선명화)
- input -> upscale -> 기능1, 기능2, 기능3, ...

### Stability AI Upscale API 
- Stability AI에서 제공하는 Upscale API 코드를 참고.
- Upscale API 호출 코드에 대한 테스트 코드 작성
- 백엔드에서 로그를 위한 Custom Exception 및 Error 코드 작성

### 결과
1. input image
![inputImage](https://github.com/chanyoungP/super-resolution/assets/67907678/d48f5a9d-6493-431a-b673-c2b1d515fe19)

2. upscaled image
![upscaledImage](https://github.com/chanyoungP/super-resolution/assets/67907678/898ebd54-0c12-4821-bb66-5bb7f6da9056)

