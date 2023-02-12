import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListRecipeFavoriteComponent } from './list-recipe-favorite.component';

describe('ListRecipeFavoriteComponent', () => {
  let component: ListRecipeFavoriteComponent;
  let fixture: ComponentFixture<ListRecipeFavoriteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListRecipeFavoriteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListRecipeFavoriteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
