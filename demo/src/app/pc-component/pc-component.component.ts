import { Component } from '@angular/core';
import {PcServiceService} from "../pc-service.service";
import {AuthService} from "../auth.service";
import {checkCompatibility} from "../utils";
@Component({
  selector: 'app-pc-component',
  templateUrl: './pc-component.component.html',
  styleUrls: ['./pc-component.component.css']
})
export class PcComponentComponent {
  list:PCComponent[] = [];
  currentPage:Pagination = {next:null, previous:null, results:[], count:0};
  compatibility:Compatibility = {status:true, message:""}
  modification: Modification = {id:0, name: "", description: "", author_name: "", likes: 0, components: []};
  constructor(public serv:PcServiceService, public auth:AuthService){}
  getList(type:string){
    this.serv.getListPCComponent(type).subscribe((data) => {
      this.currentPage = data; this.list = data.results as PCComponent[]; this.serv.load = false;});
  }
  newPage(url:string){
    this.serv.getNewPage(url).subscribe((data) => {
      this.currentPage = data; this.list = data.results as PCComponent[]; this.serv.load = false;});
  }
  add(component:PCComponent){
    this.del(component.type);
    this.modification.components.push(component);
  }
  del(type:string){
    this.modification.components = this.modification.components.filter((component)=>component.type!=type);
  }
  post(){
    this.compatibility = checkCompatibility(this.modification.components)
    if (this.compatibility.status){
      this.serv.addModification(this.modification).subscribe((data)=>console.log('Success!'));
      this.modification = {id:0, name: "", description: "", author_name: "", likes: 0,components: []};
    }
  }
}
