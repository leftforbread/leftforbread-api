import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { environment } from '../environments/environment';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { ExploreRecipesComponent } from './explore-recipes/explore-recipes.component';
import { WeeklyPlanComponent } from './weekly-plan/weekly-plan.component';
import { RecipeCardComponent } from './recipe-card/recipe-card.component';
import { ListIngredientComponent } from './list-ingredient/list-ingredient.component';
import { ListRecipeSuggestedComponent } from './list-recipe-suggested/list-recipe-suggested.component';
import { ListRecipeFavoriteComponent } from './list-recipe-favorite/list-recipe-favorite.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    ExploreRecipesComponent,
    WeeklyPlanComponent,
    RecipeCardComponent,
    ListIngredientComponent,
    ListRecipeSuggestedComponent,
    ListRecipeFavoriteComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
