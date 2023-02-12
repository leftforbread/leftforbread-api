import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListRecipeSuggestedComponent } from './list-recipe-suggested.component';

describe('ListRecipeSuggestedComponent', () => {
  let component: ListRecipeSuggestedComponent;
  let fixture: ComponentFixture<ListRecipeSuggestedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListRecipeSuggestedComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListRecipeSuggestedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
