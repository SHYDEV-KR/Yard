# 🎵 YARD

## 🗣 프로젝트 설명
[피로그래밍](https://pirogramming.com/) 16기 졸업 프로젝트로 5명이 팀을 이뤄 3~4주간 진행한 프로젝트입니다. 

인스타그램이 사진을 기반으로 하는 커뮤니티라면, YARD는 좋아하는 음악을 태그하여 다른 팬들과 소통할 수 있는 커뮤니티를 제공합니다. 

커뮤니티와 더불어 개인적으로 음악을 좋아하게 된 날짜를 기록할 수 있는 기능을 제공하여 음악마니아들이 본인의 안목을 증명할 수 있는 사이트이기도 합니다.

(현재는 비용상의 이유로 서버는 닫은 상태)


## ⚙️ 주요 기능 소개
- **게시글 CRUD** : 커뮤니티 게시글의 열람, 작성, 수정, 삭제가 가능합니다.
- **음악 데이터 활용** : 음악 API에서 데이터를 받아와 유저의 뮤직카드나 게시글 생성에 활용하였습니다.
- **해시태그** : 해시태그를 통한 특정 게시글 열람과 같은 필터링이 가능합니다.
- **AJAX** : AJAX를 활용해 커뮤니티의 좋아요가 리디렉션없이 즉시 반영됩니다.
- **유저 관련 기능** : 로그인, 소셜로그인, 회원가입, 비밀번호 수정, 유저 정보 수정 등이 가능합니다.


## ✏️ 사용된 기술종류와 기술 설명
- **Django** : 파이썬 언어 기반의 백엔드 서버 프레임워크. 서버 로직 구축, 손쉬운 DB 접근, 장고 템플릿을 통한 페이지 구성
- **HTML, CSS** : 웹사이트의 골격과 디자인
- **Vanilla Javascript** : AJAX 및 동적 웹사이트 구성
- **AWS EC2 + WSGI + NGINX** : 실제 서비스용으로 서버 배포


## 💡 사이트 이미지와 설명
### 홈
- 해시태그 추천
- 검색을 통해 원하는 태그가 포함된 게시글을 찾을 수 있습니다.
<img width="1459" alt="iShot_2022-10-12_23 00 27" src="https://user-images.githubusercontent.com/59094592/195363486-82054599-aebb-4c4b-8c91-3dc308e2580b.png">


### 음악 커뮤니티 피드
- 커뮤니티의 전체 피드를 볼 수 있으며, 원하는 해시태그로 필터링하여 게시글을 열람할 수도 있습니다.
- 마음에 드는 글에는 좋아요를 누를 수 있습니다.
<img width="1461" alt="iShot_2022-10-12_23 13 49" src="https://user-images.githubusercontent.com/59094592/195366833-1f47af31-f6b2-43aa-9faf-0bdd62af2f53.png">

### 내가 좋아한 음악들 저장
- 내가 좋아한 노래를 카드로 등록하여 프로필에 소장할 수 있습니다.
- 사이트는 유저가 어떤 노래를 언제부터 좋아했는지를 보장해줍니다.
- 시기 별로 어떤 노래를 좋아했는지도 전체적으로 열람이 가능합니다.
<img width="1460" alt="iShot_2022-10-12_23 22 20" src="https://user-images.githubusercontent.com/59094592/195368955-6a8ba897-b7cb-4876-97bb-cb756be0df61.png">

### 유저 인증 및 프로필 관련 기능
- 회원가입, 로그인 및 유저정보 수정, 이메일 인증 기능 등을 구현했습니다.
<img width="1464" alt="iShot_2022-10-12_23 31 47" src="https://user-images.githubusercontent.com/59094592/195371216-e37d14ef-f730-452a-8c08-9968350bd265.png">
<img width="1473" alt="iShot_2022-10-12_23 32 07" src="https://user-images.githubusercontent.com/59094592/195371228-bc8da6e8-8cf2-47d4-be9a-5807114de60a.png">
<img width="1475" alt="iShot_2022-10-12_23 29 55" src="https://user-images.githubusercontent.com/59094592/195370765-9063539d-a35f-4b30-a4d8-fc788a4e00a8.png">
<img width="1475" alt="iShot_2022-10-12_23 27 56" src="https://user-images.githubusercontent.com/59094592/195370519-6e2d8061-5889-4f4d-ad2a-42c0dc1a0b3d.png">
<img width="1475" alt="iShot_2022-10-12_23 30 53" src="https://user-images.githubusercontent.com/59094592/195370864-d2204c8f-6da4-463c-8f7f-4999842488e3.png">

## 🧑‍🤝‍🧑 협업방식
### Notion Workspace
- 코드작성 및 깃허브 커밋에 관련된 컨벤션을 정하고 노션에 적어두고 지키기 위해 노력했습니다.
<img width="1245" alt="iShot_2022-10-12_21 41 12" src="https://user-images.githubusercontent.com/59094592/195345288-ff1384c7-4588-4e7d-b4e2-6666c149dc32.png">


### Slack
<img width="1408" alt="iShot_2022-10-12_21 53 27" src="https://user-images.githubusercontent.com/59094592/195347669-c04ac101-8759-4b0f-8633-9fe277911ffa.png">


### Google Sheet
<img width="1066" alt="iShot_2022-10-12_21 47 44" src="https://user-images.githubusercontent.com/59094592/195346478-4c19a26a-138f-43e4-9ff0-40cef8fbf788.png">


### Figma
- 피그마에서 다같이 레이아웃을 짜고, 완성된 디자인을 참고하며 개발했습니다.

### GitHub
- 새로운 기능을 추가함에 있어 브랜치를 적극 활용했으며 브랜치명과 커밋메시지 작성 시 컨벤션을 정해서 혼선없이 작업하고자 노력했습니다.
- 풀리퀘스트와 머지 전에 코드리뷰를 활용해봤습니다.


## 🛠 To Dos (개선할 점)
- [ ] 반응형 지원
- [ ] 미완성 기능 구현
- [ ] 디자인 개선
- [ ] 자체 음원 DB 구축
