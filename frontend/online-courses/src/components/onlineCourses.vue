<template>
<section class="my-sect">
  <!-- Start navbar section -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid d-flex">
    <a class="navbar-brand fw-bold" href="#">
      Udemy
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Categories
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">IT</a></li>
            <li><a class="dropdown-item" href="#">DEVELOPMENT</a></li>
            <li><a class="dropdown-item" href="#">MANAGMENT</a></li>
    
          </ul>
        </li>
        
      </ul>
      <input  class="form-control me-2 my-input" type="search" v-model="data_input"  @keyup.enter="searchFlag()" placeholder="Search for Anything" aria-label="Search">
      <form class="d-flex" role="search" style="width: 55%;">
        <span class="sp1">Udemy business</span>
        <span class="sp2"> Teach on Udemy</span>
        <i class="fa-solid fa-cart-shopping"></i>
        <button class="my-btn my-btn1" type="submit">Log in</button>
        <button class="my-btn my-btn2" type="submit">Sign up</button>
        <i class="fa-solid fa-globe icon1"></i>
      </form>
    </div>
  </div>
</nav>
<div class="body container d-flex mt-5">
  <div class="filter-section me-3" style="width: 20%;">
    <div style="border-top: 1px solid #eee ; padding-top: 10px;">
  <a class=" text-decoration-none"  aria-expanded="false" style="color: black">
    Categories
  </a>
  <ul class="ps-2"  style="margin-top: 15px;">
    <li>
      <input  v-model="checkedNames" value="1" type="checkbox" @change="getCourses(getStr(checkedNames))">
      <label for="it">IT</label>
    </li>
    
    <li>
      <input   v-model="checkedNames" value="2" type="checkbox" @change="getCourses(getStr(checkedNames))">
      <label for="dev">DEVELOPMENT</label>
    </li>
    
    <li>
      <input   v-model="checkedNames" value="3" type="checkbox" @change="getCourses(getStr(checkedNames))">
      <label for="man" >MANAGMENT</label>
    </li>
    
  </ul>
    </div>
    <div class="pb-3" style="border-top: 1px solid #eee ; padding-top: 10px;">
  <a class=" text-decoration-none" aria-expanded="false" style="color: black">
    price
  </a>
  <ul class="ps-2" style="margin-top: 15px;">
    <li>
      <input type="checkbox" v-model="checkedNames" value='10' @change="getCourses(getStr(checkedNames))">
      <label>10$</label>
    </li>
    <li>
      <input type="checkbox" v-model="checkedNames" value='20' @change="getCourses(getStr(checkedNames))">
      <label>20$</label>
    </li>
    <li>
      <input type="checkbox" v-model="checkedNames" value='40' @change="getCourses(getStr(checkedNames))">
      <label>40$</label>
    </li>
  </ul>
</div>
  </div>
<div class="search-result" style="width:100%;">
  
  <div class="my-card" v-for="item in course.results" :key="item.id">
    <div class="img-card">
      <img :src="item.image"  alt="">
    </div>
       
    <div class="body-card">
      <h2 class="title-card">{{item.name}}</h2>
      <h6 class="subtitle-card">{{item.subtitle}}</h6>
      <p class="text-card">{{item.description}}</p>
      <span  class="cat-card">Cat : {{item.categorie}}</span>
      <br>
      
        <span class="price-card">{{item.price}}$</span>
        <a href="#">show details</a>
        
      
      
    </div>
</div>
    
  </div>

</div>
  <!-- end navbar section -->
  <!-- section of pagination -->
  <!-- <div class="container">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
  </div> -->
  <div class="pagination-container p-3">
    <button @click="prevPage" :disabled="currentPage === 1" class="pagination-button">Previous</button>
    <span class="pagination-info">Page {{ currentPage }} of {{ totalPages }}</span>
    <button @click="nextPage" :disabled="currentPage === totalPages" class="pagination-button">Next</button>
  </div>

</section>
</template>

<script>
import { ref } from 'vue' 

import axios from 'axios';
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  data(){
    return {
      name : "courseApp",
      course : [],
      data_input : '',
      flag : false,
      checkedNames : ref([]),
      itemsPerPage: 5, // Number of items to display per page
      currentPage: 1,  // Current page
      
     

    }
  },

  mounted(){
    this.getCourses("");
  },
  computed: {
    // Calculate the total number of pages
    totalPages() {
      return Math.ceil(this.course.count / this.itemsPerPage);   
    },
  

  },


  methods: {
    getStr(myDic){
      var path = '';
      for (var key in myDic) {
            
          console.log("Key: " + key + ", Value: " + myDic[key]);
          if (key == 0) {
            if (myDic[key] == 10 || myDic[key]==20 || myDic[key]==40) {
              path += "price="+myDic[key]
            }
            else {
              path += "categorie="+myDic[key]
            }
            

          }
          else {
            if (myDic[key] == 10 || myDic[key]==20 || myDic[key]==40) {
              path += "&price="+myDic[key]
            }
            else {
              path += "&categorie="+myDic[key]
            }
            
          }
          
          console.log(myDic[key])
          }
      console.log(path)
      return path
        },

    getCourses(s){
      axios({
        method:"get",
        url:'http://127.0.0.1:8000/course/api/list?'+s,
      }).then(response => this.course = response.data);
           
    },

    searchFlag(){
      this.flag=true;
      this.getCourses('search='+this.data_input)
    },

    // pagination methods
    prevPage() {
      if (this.currentPage > 1) {
        //this.getCourses("limit=5");
        axios({
        method:"get",
        url:this.course.previous,
        //url:'http://127.0.0.1:8000/course/api/list?'+s+"limit=5&offset=5"
      }).then(response => this.course = response.data);
        this.currentPage--;
        console.log(this.course.previous)
      }
    },
    // Go to the next page
    nextPage() {
      if (this.currentPage < this.totalPages) {
        //this.getCourses("limit=5&offset=5");
        axios({
        method:"get",
        url:this.course.next,
        //url:'http://127.0.0.1:8000/course/api/list?'+s+"limit=5"
      }).then(response => this.course = response.data);
        this.currentPage++;
        console.log(this.course.next)
        
        
      }
    }

  },
  
}
</script>










<style scoped>
ul{
  list-style: none;
  color: #444;
}

ul li label{
  margin-left: 5px;
  


}
.my-logo {
  width: 70px;
  height: 70px;
}
.sp1 , .sp2{
  margin-top: 5px;
  margin-right: 5px;
  margin-left: 10px;
  font-size: 12px;
  font-weight: 400;
}
.fa-cart-shopping {
  margin-top:5px;
  margin-left: 5px;
  margin-right: 10px;
}
.my-btn {
  margin-right: 5px;
  border: 1px solid black;
  font-size: 12px;
  padding: 5px 5px;
  width: 80px;
  height: 30px;
  
}

.fa-globe {
  margin-left: 10px;
  border: 1px solid black;
  padding: 5px 5px;
  height: 30px;

}

.my-btn2 {
  margin-left: 5px;
  background-color: black;
  color: white;
}
.my-btn1 {
  margin-left: 10px;
}
.my-input[placeholder]{
  font-size: 12px;
  font-family: 400;
}

.my-drop li span  {
  margin-left: 10px;
  
}

a {
  text-decoration: none;
}

.my-card {
  display: flex;
  border: 1px solid #eee;
  margin-bottom: 20px;
  border-radius: 4px;

}
.my-card .img-card {
  width: 30%;
}

.my-card .img-card img {
  width: 300px;
  height: 250px;
}

.my-card .body-card{
  width: 60%;
  padding-top: 20px;
  padding-bottom: 10px;
}
.body-card .title-card{
  font-size: 30px;
  color: #333;
  margin-bottom: 15px;
}
.body-card .subtitle-card {
  font-size: 20px;
  margin-bottom: 15px;
  color: #777;

}

.body-card .text-card {
  font-size: 15px;
  color: #444
}

.body-card .cat-card {
  font-size: 15px;
  color : #555;
  margin-bottom: 20px;
  display: inline-block;
}

.body-card .price-card {
  color: white;
  background-color: #ddd;
  font-size: 15px;
  border-radius: 5px;
  font-weight: bold;
  padding: 6px 10px;
  
}
.body-card a {
  text-decoration: none;
  color: white;
  background-color: #ddd;
  padding: 6px 10px;
  border-radius: 5px;
  font-size: 15px;
  margin-left: 15px;
  cursor: pointer;
}
/* style of pagination */
.pagination-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px 0;
}

.pagination-button {
  padding: 8px 12px;
  background-color: #333;
  color: #fff;
  border: 1px solid #007bff;
  border-radius: 4px;
  cursor: pointer;
}

.pagination-button:disabled {
  background-color: #ccc;
  color: #666;
  border: 1px solid #ccc;
  cursor: not-allowed;
}

.pagination-info {
  font-size: 16px;
}
</style>


