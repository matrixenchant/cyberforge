import { Component } from '@angular/core';
import {PcServiceService} from "../pc-service.service";
import {AuthService} from "../auth.service";

@Component({
  selector: 'app-constructor',
  templateUrl: './constructor.component.html',
  styleUrls: ['./constructor.component.css']
})
export class ConstructorComponent {
  modifications:Modification[] = [];
  currentPage:Pagination = {next:null, previous:null, results:[], count:0};
  constructor(public serv:PcServiceService, public auth:AuthService) {
  }
  ngOnInit(){
    this.serv.getListModification().subscribe((data) => {
      this.currentPage=data; this.modifications=data.results as Modification[]; this.serv.load = false;});
  }
  newPage(url:string){
    this.serv.getNewPage(url).subscribe((data) => {
      this.currentPage = data; this.modifications = data.results as Modification[]; this.serv.load = false;});
  }
  like(modification:Modification){
    this.serv.updateModification(modification).subscribe((data) => modification.likes = data.likes)
  }
  delete(id:number){
    this.serv.deleteModification(id).subscribe(()=>this.modifications = this.modifications.filter(
      (data)=>data.id != id))
  }
}
