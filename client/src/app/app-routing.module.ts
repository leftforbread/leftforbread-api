import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ExploreRecipesComponent } from './explore-recipes/explore-recipes.component';
import { WeeklyPlanComponent } from './weekly-plan/weekly-plan.component';

const routes: Routes = [
  {
    path: '',
    component: ExploreRecipesComponent
  },
  {
    path: 'weekly-plan',
    component: WeeklyPlanComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
