import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {MainComponent} from "./main/main.component";
import {ErrorComponent} from "./error/error.component";
import {ConstructorComponent} from "./constructor/constructor.component";
import {LoginComponent} from "./login/login.component";

const routes: Routes = [
  {path:'main',component:MainComponent},
  {path:'main/constructor',component:ConstructorComponent},
  {path:'login',component:LoginComponent},
  {path:'', redirectTo:'main', pathMatch:'full'},
  {path:'**',component:ErrorComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
